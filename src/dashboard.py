from src.ideas import IdeaManager

class Dashboard:
    def __init__(self, idea_manager: IdeaManager):
        self.idea_manager = idea_manager

    def display_ideas(self, user_id: str) -> None:
        ideas = self.idea_manager.get_all_ideas(user_id)
        if not ideas:
            print("No ideas found for this user.")
            return
        print("Your Ideas:")
        for idea in ideas:
            print(f"ID: {idea.id}, Title: {idea.title}, Status: {idea.status.value}, Description: {idea.description}")
