import os
import random
import logging
# from groq import Groq  # Uncomment if using Groq
from config import BASE_DIR

logger = logging.getLogger(__name__)

class ContentGenerator:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = None
        if self.api_key:
            # self.client = Groq(api_key=self.api_key) # Uncomment to use real API
            pass
        
    def generate_text(self, prompt_template, context, max_tokens=100):
        """
        Generates text using LLM or falls back to templates if no key/client.
        """
        if self.client:
            try:
                # Placeholder for actual API call
                # chat_completion = self.client.chat.completions.create(...)
                # return chat_completion.choices[0].message.content
                pass
            except Exception as e:
                logger.error(f"LLM Error: {e}")
        
        # Fallback Logic (Deterministic generation for Demo)
        return self._fallback_generator(prompt_template, context)

    def _fallback_generator(self, template_name, context):
        """Simple template-based generator for demo purposes."""
        if "task" in template_name:
            actions = ["Update", "Fix", "Refactor", "Design", "Implement", "Test"]
            nouns = ["API", "Button", "Database", "Login", "Header", "Cache"]
            return f"{random.choice(actions)} {random.choice(nouns)} for {context.get('project_name', 'Project')}"
        
        if "description" in template_name:
            return f"This is a simulated description for {context.get('item_name', 'item')}. Please ensure this is completed by EOD."
            
        return "Generated Content"