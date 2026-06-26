import argparse
from src.ideas import IdeaManager, IdeaStatus
from src.dashboard import Dashboard

def add_idea(user_id, title, description, status="Draft"):
    manager = IdeaManager()
    idea_id = manager.add_idea(user_id, title, description, IdeaStatus(status))
    print(f"Idea added with ID: {idea_id}")

def view_ideas(user_id):
    manager = IdeaManager()
    dashboard = Dashboard(manager)
    dashboard.display_ideas(user_id)

def main():
    parser = argparse.ArgumentParser(description="Idea-Fathom: Manage user ideas.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    add_parser = subparsers.add_parser("add_idea", help="Add a new idea")
    add_parser.add_argument("user_id", help="User ID")
    add_parser.add_argument("title", help="Idea title")
    add_parser.add_argument("description", help="Idea description")
    add_parser.add_argument("--status", choices=["Draft", "In Ideation", "Validated", "Rejected"], default="Draft", help="Initial status")
    view_parser = subparsers.add_parser("view_ideas", help="View user's ideas")
    view_parser.add_argument("user_id", help="User ID")
    args = parser.parse_args()
    if args.command == "add_idea":
        add_idea(args.user_id, args.title, args.description, args.status)
    elif args.command == "view_ideas":
        view_ideas(args.user_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
