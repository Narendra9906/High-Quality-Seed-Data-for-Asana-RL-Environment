"""
LLM utilities for generating realistic text content.
Supports Groq API.
"""

import os
import logging
import random
from typing import List, Optional
import time

import config

logger = logging.getLogger(__name__)

# Try to import groq
try:
    from groq import Groq
    GROQ_AVAILABLE = True
except ImportError:
    GROQ_AVAILABLE = False
    logger.warning("Groq package not installed. Using fallback text generation.")


class LLMClient:
    """Client for LLM-based text generation."""
    
    def __init__(self):
        self.enabled = config.ENABLE_LLM
        self.client = None
        
        if self.enabled and GROQ_AVAILABLE and config.GROQ_API_KEY:
            try:
                self.client = Groq(api_key=config.GROQ_API_KEY)
                logger.info("Groq client initialized successfully")
            except Exception as e:
                logger.warning(f"Failed to initialize Groq client: {e}")
                self.enabled = False
        else:
            self.enabled = False
            logger.info("LLM disabled or not configured. Using fallback generation.")
    
    def generate(
        self, 
        prompt: str, 
        max_tokens: int = None,
        temperature: float = None
    ) -> str:
        """
        Generate text using LLM.
        
        Args:
            prompt: The prompt to send to the LLM
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature
            
        Returns:
            Generated text string
        """
        if not self.enabled or not self.client:
            return self._fallback_generate(prompt)
        
        max_tokens = max_tokens or config.LLM_MAX_TOKENS
        temperature = temperature or config.LLM_TEMPERATURE
        
        try:
            response = self.client.chat.completions.create(
                model=config.GROQ_MODEL,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=temperature
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.warning(f"LLM generation failed: {e}. Using fallback.")
            return self._fallback_generate(prompt)
    
    def generate_batch(
        self, 
        prompts: List[str], 
        delay: float = 0.5
    ) -> List[str]:
        """
        Generate text for multiple prompts with rate limiting.
        
        Args:
            prompts: List of prompts
            delay: Delay between requests in seconds
            
        Returns:
            List of generated texts
        """
        results = []
        for i, prompt in enumerate(prompts):
            result = self.generate(prompt)
            results.append(result)
            if i < len(prompts) - 1:
                time.sleep(delay)
        return results
    
    def _fallback_generate(self, prompt: str) -> str:
        """Generate fallback text when LLM is not available."""
        # Parse prompt to understand context
        prompt_lower = prompt.lower()
        
        if "task name" in prompt_lower or "task title" in prompt_lower:
            return self._generate_fallback_task_name(prompt)
        elif "description" in prompt_lower:
            return self._generate_fallback_description(prompt)
        elif "comment" in prompt_lower:
            return self._generate_fallback_comment()
        else:
            return "Generated content placeholder"
    
    def _generate_fallback_task_name(self, prompt: str) -> str:
        """Generate fallback task name."""
        engineering_tasks = [
            "Implement user authentication flow",
            "Fix database connection pooling issue",
            "Add unit tests for payment module",
            "Refactor API error handling",
            "Update dependency versions",
            "Optimize database queries for dashboard",
            "Add logging to background workers",
            "Fix race condition in checkout process",
            "Implement rate limiting for API",
            "Add caching layer for user sessions",
            "Review and update API documentation",
            "Fix memory leak in image processing",
            "Implement webhook retry mechanism",
            "Add monitoring alerts for critical paths",
            "Migrate legacy code to new framework"
        ]
        
        marketing_tasks = [
            "Create Q3 campaign assets",
            "Update landing page copy",
            "Design email newsletter template",
            "Analyze competitor pricing strategies",
            "Write blog post on industry trends",
            "Schedule social media content",
            "Review ad campaign performance",
            "Create customer case study",
            "Update brand guidelines document",
            "Plan webinar content and slides"
        ]
        
        operations_tasks = [
            "Process monthly invoices",
            "Update vendor contracts",
            "Review compliance documentation",
            "Conduct security audit review",
            "Update employee handbook",
            "Process customer refund requests",
            "Prepare quarterly report",
            "Coordinate team training session",
            "Review and approve expenses",
            "Update internal wiki documentation"
        ]
        
        if "engineering" in prompt.lower() or "technical" in prompt.lower():
            return random.choice(engineering_tasks)
        elif "marketing" in prompt.lower():
            return random.choice(marketing_tasks)
        elif "operations" in prompt.lower():
            return random.choice(operations_tasks)
        else:
            all_tasks = engineering_tasks + marketing_tasks + operations_tasks
            return random.choice(all_tasks)
    
    def _generate_fallback_description(self, prompt: str) -> str:
        """Generate fallback task description."""
        descriptions = [
            "",  # 20% empty
            "",
            "This task needs to be completed by end of sprint.",
            "Follow up on the previous discussion and implement changes.",
            "Review the requirements document before starting.",
            "Coordinate with the team lead for clarifications.",
            """This is a detailed task that requires:
- Review of existing implementation
- Analysis of edge cases
- Unit test coverage
- Documentation updates""",
            "See attached specifications for details. Reach out if any questions.",
            "Priority task for this sprint. Block time on calendar.",
            "Dependency on API team. Check status before starting."
        ]
        return random.choice(descriptions)
    
    def _generate_fallback_comment(self) -> str:
        """Generate fallback comment."""
        comments = [
            "Started working on this.",
            "Made good progress today. Should be done by tomorrow.",
            "Blocked on external dependency. Following up.",
            "Completed the initial implementation. Ready for review.",
            "Found some edge cases that need discussion.",
            "Updated the approach based on feedback.",
            "@team - please review when you get a chance",
            "This is taking longer than expected due to complexity.",
            "Done! Moving to the next task.",
            "Need clarification on the requirements.",
            "Pushed initial changes. Will continue tomorrow.",
            "Had to refactor some existing code first.",
            "All tests passing now.",
            "Deployed to staging for testing.",
            "Fixed the issues from code review."
        ]
        return random.choice(comments)


# Singleton instance
_llm_client = None


def get_llm_client() -> LLMClient:
    """Get or create LLM client singleton."""
    global _llm_client
    if _llm_client is None:
        _llm_client = LLMClient()
    return _llm_client