# newsletter/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Subscriber
from .forms import SubscribeForm

class NewsletterFunctionalityTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.subscribe_url = reverse('newsletter:subscribe')
    
    def test_subscribe_creates_user(self):
        """Test that subscription creates a user in database"""
        # Test with valid data
        response = self.client.post(self.subscribe_url, {
            'email': 'test@example.com',
            'first_name': 'Test',
            'last_name': 'User'
        })
        
        # Check redirect happened (301 or 302 are both acceptable)
        self.assertIn(response.status_code, [301, 302])
        
        # Check user was created
        self.assertTrue(Subscriber.objects.filter(email='test@example.com').exists())
        subscriber = Subscriber.objects.get(email='test@example.com')
        self.assertEqual(subscriber.first_name, 'Test')
        self.assertEqual(subscriber.last_name, 'User')
        self.assertTrue(subscriber.subscribed)
    
    def test_subscribe_without_optional_fields(self):
        """Test subscription with only required email field"""
        response = self.client.post(self.subscribe_url, {
            'email': 'simple@example.com'
        })
        
        self.assertIn(response.status_code, [301, 302])
        self.assertTrue(Subscriber.objects.filter(email='simple@example.com').exists())
    
    def test_duplicate_email(self):
        """Test subscribing with existing email"""
        # Create existing subscriber
        Subscriber.objects.create(
            email='existing@example.com',
            first_name='John',
            last_name='Doe'
        )
        
        response = self.client.post(self.subscribe_url, {
            'email': 'existing@example.com',
            'first_name': 'Jane',  # Different name
            'last_name': 'Smith'
        })
        
        self.assertIn(response.status_code, [301, 302])
        
        # Should still have the original subscriber data
        subscriber = Subscriber.objects.get(email='existing@example.com')
        self.assertEqual(subscriber.first_name, 'John')  # Original name preserved
        self.assertEqual(subscriber.last_name, 'Doe')
    
    def test_unsubscribe_functionality(self):
        """Test unsubscribe functionality"""
        # Create a subscribed user
        subscriber = Subscriber.objects.create(
            email='test@example.com',
            subscribed=True
        )
        
        unsubscribe_url = reverse('newsletter:unsubscribe', args=['test@example.com'])
        response = self.client.post(unsubscribe_url)
        
        self.assertIn(response.status_code, [301, 302])
        
        # Check user was unsubscribed
        subscriber.refresh_from_db()
        self.assertFalse(subscriber.subscribed)

class SubscribeFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        form = SubscribeForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_invalid_email(self):
        form_data = {
            'email': 'invalid-email',
            'first_name': 'John'
        }
        form = SubscribeForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

# Add this test to verify your actual view logic
class ViewLogicTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.subscribe_url = reverse('newsletter:subscribe')
    
    def test_new_subscription_flow(self):
        """Test the complete flow for a new subscription"""
        response = self.client.post(self.subscribe_url, {
            'email': 'newuser@example.com',
            'first_name': 'New',
            'last_name': 'User'
        })
        
        # Should redirect
        self.assertIn(response.status_code, [301, 302])
        
        # Check subscriber was created with correct data
        subscriber = Subscriber.objects.get(email='newuser@example.com')
        self.assertEqual(subscriber.first_name, 'New')
        self.assertEqual(subscriber.last_name, 'User')
        self.assertTrue(subscriber.subscribed)
    
    def test_existing_subscribed_user(self):
        """Test behavior when user is already subscribed"""
        # Create already subscribed user
        Subscriber.objects.create(
            email='existing@example.com',
            first_name='Existing',
            last_name='User',
            subscribed=True
        )
        
        response = self.client.post(self.subscribe_url, {
            'email': 'existing@example.com',
            'first_name': 'Different',  # Should be ignored
            'last_name': 'Name'
        })
        
        self.assertIn(response.status_code, [301, 302])
        
        # User should still exist with original data
        subscriber = Subscriber.objects.get(email='existing@example.com')
        self.assertEqual(subscriber.first_name, 'Existing')  # Original preserved
        self.assertEqual(subscriber.last_name, 'User')
        self.assertTrue(subscriber.subscribed)  # Still subscribed
    
    def test_resubscribe_flow(self):
        """Test resubscribing an unsubscribed user"""
        # Create unsubscribed user
        Subscriber.objects.create(
            email='unsubscribed@example.com',
            first_name='Old',
            last_name='User',
            subscribed=False
        )
        
        response = self.client.post(self.subscribe_url, {
            'email': 'unsubscribed@example.com',
            'first_name': 'Resubscribed',
            'last_name': 'User'
        })
        
        self.assertIn(response.status_code, [301, 302])
        
        # User should be resubscribed but name unchanged (due to get_or_create)
        subscriber = Subscriber.objects.get(email='unsubscribed@example.com')
        self.assertTrue(subscriber.subscribed)  # Now subscribed again
        # Note: The name won't change due to get_or_create logic