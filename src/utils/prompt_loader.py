"""
Prompt loading and management utilities.
"""

import os
from pathlib import Path
from typing import Dict, Optional
import logging

logger = logging.getLogger(__name__)


class PromptLoader:
    """Loads and manages LLM prompts from files."""
    
    def __init__(self, prompts_dir: str = "prompts"):
        """
        Initialize prompt loader.
        
        Args:
            prompts_dir: Directory containing prompt files
        """
        self.prompts_dir = Path(prompts_dir)
        self.cache: Dict[str, str] = {}
        
        # Create prompts directory if it doesn't exist
        self.prompts_dir.mkdir(parents=True, exist_ok=True)
        
        # Load all prompts
        self._load_all_prompts()
    
    def _load_all_prompts(self):
        """Load all prompt files into cache."""
        if not self.prompts_dir.exists():
            logger.warning(f"Prompts directory not found: {self.prompts_dir}")
            return
        
        for prompt_file in self.prompts_dir.glob("*.txt"):
            try:
                with open(prompt_file, 'r') as f:
                    self.cache[prompt_file.stem] = f.read().strip()
                logger.debug(f"Loaded prompt: {prompt_file.stem}")
            except Exception as e:
                logger.warning(f"Error loading prompt {prompt_file}: {e}")
    
    def get(self, prompt_name: str) -> Optional[str]:
        """
        Get a prompt by name.
        
        Args:
            prompt_name: Name of the prompt (filename without .txt)
            
        Returns:
            Prompt string or None if not found
        """
        return self.cache.get(prompt_name)
    
    def format(self, prompt_name: str, **kwargs) -> Optional[str]:
        """
        Get and format a prompt with variables.
        
        Args:
            prompt_name: Name of the prompt
            **kwargs: Variables to substitute in the prompt
            
        Returns:
            Formatted prompt string or None if not found
        """
        prompt = self.get(prompt_name)
        if prompt is None:
            return None
        
        try:
            return prompt.format(**kwargs)
        except KeyError as e:
            logger.warning(f"Missing variable in prompt {prompt_name}: {e}")
            return prompt


# Default prompts to create if files don't exist
DEFAULT_PROMPTS = {
    "tasks_engineering": """Generate a realistic engineering task name for a {project_type} project.
The task should be related to {focus_area}.
The team uses Agile/Scrum methodology.

Output only the task name, no other text.
Examples:
- Implement user authentication flow
- Fix database connection pooling issue
- Add unit tests for payment module""",

    "tasks_marketing": """Generate a realistic marketing task name for a {initiative_type} initiative.
The task should be related to {focus_area}.

Output only the task name, no other text.
Examples:
- Create Q3 campaign landing page
- Update social media content calendar
- Design email newsletter template""",

    "tasks_operations": """Generate a realistic operations task name for {focus_area}.
This is for a B2B SaaS company's operations team.

Output only the task name, no other text.
Examples:
- Process monthly vendor invoices
- Update customer support documentation
- Review compliance audit findings""",

    "task_descriptions": """Generate a realistic task description for a task named: "{task_name}"
The task belongs to a {project_type} project.

Guidelines:
- 20% of descriptions should be empty
- 50% should be 1-3 sentences
- 30% should be detailed with bullet points

Output only the description, no other text.""",

    "comments": """Generate a realistic comment for a task named: "{task_name}"
The commenter's name is {commenter_name}.
The task status is: {task_status}

Guidelines:
- Comment should be professional but conversational
- May include status updates, questions, or feedback
- Keep it under 2-3 sentences usually

Output only the comment text, no other text.""",

    "project_names": """Generate a realistic project name for a {team_type} team working on {initiative_name}.
The project should sound professional and be suitable for a B2B SaaS company.

Output only the project name, no other text.
Examples:
- Q3 Platform Modernization
- Customer Portal Redesign
- API Gateway Implementation"""
}


def ensure_default_prompts():
    """Create default prompt files if they don't exist."""
    prompts_dir = Path("prompts")
    prompts_dir.mkdir(parents=True, exist_ok=True)
    
    for name, content in DEFAULT_PROMPTS.items():
        prompt_file = prompts_dir / f"{name}.txt"
        if not prompt_file.exists():
            with open(prompt_file, 'w') as f:
                f.write(content)
            logger.info(f"Created default prompt: {name}.txt")


# Singleton instance
_prompt_loader = None


def get_prompt_loader() -> PromptLoader:
    """Get or create prompt loader singleton."""
    global _prompt_loader
    if _prompt_loader is None:
        ensure_default_prompts()
        _prompt_loader = PromptLoader()
    return _prompt_loader