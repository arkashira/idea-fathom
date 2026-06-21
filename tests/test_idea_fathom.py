from idea_fathom import IdeaFathom, Idea, Comment, Suggestion

def test_publish_idea():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    assert idea.title == "Test Idea"
    assert idea.description == "This is a test idea"
    assert idea.anonymous == False
    assert idea.comments == []
    assert idea.upvotes == 0
    assert idea.suggestions == []

def test_comment_on_idea():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    comment = idea_fathom.comment_on_idea(idea.id, "This is a test comment")
    assert comment.text == "This is a test comment"
    assert comment.idea_id == idea.id
    assert idea.comments[0].text == "This is a test comment"

def test_suggest_improvement():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    suggestion = idea_fathom.suggest_improvement(idea.id, "This is a test suggestion")
    assert suggestion.text == "This is a test suggestion"
    assert suggestion.idea_id == idea.id
    assert idea.suggestions[0].text == "This is a test suggestion"

def test_upvote_idea():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    idea_fathom.upvote_idea(idea.id)
    assert idea.upvotes == 1

def test_get_idea():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    retrieved_idea = idea_fathom.get_idea(idea.id)
    assert retrieved_idea.title == "Test Idea"
    assert retrieved_idea.description == "This is a test idea"

def test_get_comments():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    comment1 = idea_fathom.comment_on_idea(idea.id, "This is a test comment 1")
    comment2 = idea_fathom.comment_on_idea(idea.id, "This is a test comment 2")
    comments = idea_fathom.get_comments(idea.id)
    assert len(comments) == 2
    assert comments[0].text == "This is a test comment 1"
    assert comments[1].text == "This is a test comment 2"

def test_get_suggestions():
    idea_fathom = IdeaFathom()
    idea = idea_fathom.publish_idea("Test Idea", "This is a test idea")
    suggestion1 = idea_fathom.suggest_improvement(idea.id, "This is a test suggestion 1")
    suggestion2 = idea_fathom.suggest_improvement(idea.id, "This is a test suggestion 2")
    suggestions = idea_fathom.get_suggestions(idea.id)
    assert len(suggestions) == 2
    assert suggestions[0].text == "This is a test suggestion 1"
    assert suggestions[1].text == "This is a test suggestion 2"
