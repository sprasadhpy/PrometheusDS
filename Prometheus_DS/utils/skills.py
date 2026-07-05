"""
Skill loader for PrometheusDS agents.

Skills are markdown files that provide agents with reusable knowledge:
- strategies/ : What to do (cleaning approaches, patterns)
- patterns/   : How to do it (code templates for common operations)
- errors/     : Known error fixes (pre-written solutions for common failures)

Usage:
    from Prometheus_DS.utils.skills import load_skills

    # Load all skills for the data cleaning agent
    all_skills = load_skills("data_cleaning")

    # Load only strategies
    strategies = load_skills("data_cleaning", category="strategies")

    # Load only error patterns
    error_fixes = load_skills("data_cleaning", category="errors")
"""

import os
from typing import Optional


SKILLS_DIR = os.path.join(os.path.dirname(__file__), "..", "agents", "skills")


def load_skills(agent_name: str, category: Optional[str] = None) -> str:
    """
    Load skill files for a given agent.

    Parameters
    ----------
    agent_name : str
        Name of the agent (e.g., "data_cleaning").
    category : str, optional
        Specific category to load ("strategies", "patterns", "errors").
        If None, loads all categories.

    Returns
    -------
    str
        Combined content of all matching .md files, separated by headers.
    """
    agent_skills_dir = os.path.join(SKILLS_DIR, agent_name)

    if not os.path.exists(agent_skills_dir):
        return ""

    sections = []

    if category:
        # Load specific category
        cat_dir = os.path.join(agent_skills_dir, category)
        if os.path.exists(cat_dir):
            sections.extend(_load_directory(cat_dir))
    else:
        # Load all categories
        for item in sorted(os.listdir(agent_skills_dir)):
            item_path = os.path.join(agent_skills_dir, item)
            if os.path.isdir(item_path):
                sections.append(f"\n{'='*60}")
                sections.append(f"## {item.upper()}")
                sections.append(f"{'='*60}\n")
                sections.extend(_load_directory(item_path))
            elif item.endswith(".md"):
                sections.append(_read_file(item_path))

    return "\n\n".join(sections)


def load_error_skills(agent_name: str) -> str:
    """Load only error-fix skills for an agent."""
    return load_skills(agent_name, category="errors")


def load_strategy_skills(agent_name: str) -> str:
    """Load only strategy skills for an agent."""
    return load_skills(agent_name, category="strategies")


def load_pattern_skills(agent_name: str) -> str:
    """Load only pattern/code-template skills for an agent."""
    return load_skills(agent_name, category="patterns")


def _load_directory(directory: str) -> list:
    """Load all .md files from a directory."""
    contents = []
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            contents.append(_read_file(filepath))
    return contents


def _read_file(filepath: str) -> str:
    """Read a single file and return its content."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read().strip()
