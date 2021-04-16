"""Seed file to make sample data for db."""
from models import db, connect_db, User, Post, Tag, PostTag


def run_seed():
    # Create all tables
    db.drop_all()
    db.create_all()

    User.query.delete()
    Post.query.delete()
    Tag.query.delete()
    PostTag.query.delete()

    # Make a bunch of Users

    u1 = User(first_name="John", last_name="Jackson", image_url="https://picsum.photos/id/1011/300/300")
    u2 = User(first_name="Kick", last_name="Buttski", image_url="https://picsum.photos/id/433/300/300")
    u3 = User(first_name="Jim", last_name="Johnson", image_url="https://picsum.photos/id/237/300/300")
    u4 = User(first_name="Turd", last_name="Ferguson", image_url="https://picsum.photos/id/1062/300/300")
    u5 = User(first_name="Jack", last_name="Jameson", image_url="https://picsum.photos/id/659/300/300")

    db.session.add_all([u1, u2, u3, u4, u5])
    db.session.commit()



    # Make a bunch of Posts

    # John Jackson's posts
    p1 = Post(title="This is My the first Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=1)

    p2 = Post(title="What's happening now, Post Two", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=1)

    p3 = Post(title="I gotta another post, three", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=1)


    # Kick Buttski's posts
    p4 = Post(title="How to kick butt, Part One", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=2)

    p5 = Post(title="How to kick butt, Part Two", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=2)

    p6 = Post(title="I would win in fight with a bear, here's why...", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=2)


    p7 = Post(title="How I think I would beat up Chuck Norris", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=2)


    # Jim Johnson's posts
    p8 = Post(title="This is My the first Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=3)

    p9 = Post(title="What's happening now, Post Two", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=3)

    p10 = Post(title="I gotta another post, three", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=3)


    # Turd Ferguson's posts
    p11 = Post(title="Hey, It's me, Turd.", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=4)

    p12 = Post(title="My famous Mac and Cheese Recipe", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=4)

    p13 = Post(title="How to make a sandwich", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=4)

    p14 = Post(title="My two cents on tacos", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=4)


    # Jack Jameson's posts
    p15 = Post(title="This is My the first Post", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=5)

    p16 = Post(title="What's happening now, Post Two", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=5)

    p17= Post(title="I gotta another post, three", content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.", user_id=5)


    db.session.add_all([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17])
    db.session.commit()



    # Make a bunch of Tags

    t1 = Tag(name="Fun")
    t2 = Tag(name="Cool") 
    t3 = Tag(name="Food") 
    t4 = Tag(name="Boring")
    t5 = Tag(name="Stuff")
    t6 = Tag(name="Cheese")


    db.session.add_all([t1, t2, t3, t4, t5, t6])
    db.session.commit()



    # Make a bunch of PostTags

    # John Jackson's posts
    pt1 = PostTag(post_id=1, tag_id=4)
    pt2 = PostTag(post_id=1, tag_id=5)

    pt3 = PostTag(post_id=2, tag_id=4)
    pt4 = PostTag(post_id=2, tag_id=5)

    pt5 = PostTag(post_id=3, tag_id=4)
    pt6 = PostTag(post_id=3, tag_id=5)


    # Kick Buttski's posts
    pt7 = PostTag(post_id=4, tag_id=1)
    pt8 = PostTag(post_id=4, tag_id=2)
    pt9 = PostTag(post_id=4, tag_id=5)

    pt10 = PostTag(post_id=5, tag_id=1)
    pt11 = PostTag(post_id=5, tag_id=2)

    pt12 = PostTag(post_id=6, tag_id=1)
    pt13 = PostTag(post_id=6, tag_id=2)
    pt14 = PostTag(post_id=6, tag_id=5)

    pt15 = PostTag(post_id=7, tag_id=4)


    # Jim Johnson's posts
    pt16 = PostTag(post_id=8, tag_id=4)
    pt17 = PostTag(post_id=8, tag_id=5)

    pt18 = PostTag(post_id=9, tag_id=4)
    pt19 = PostTag(post_id=9, tag_id=5)

    pt20 = PostTag(post_id=10, tag_id=4)
    pt21 = PostTag(post_id=10, tag_id=5)


    # Turd Ferguson's posts
    pt22 = PostTag(post_id=11, tag_id=1)
    pt23 = PostTag(post_id=11, tag_id=2)
    pt24 = PostTag(post_id=11, tag_id=5)

    pt25 = PostTag(post_id=12, tag_id=1)
    pt26 = PostTag(post_id=12, tag_id=3)
    pt27 = PostTag(post_id=12, tag_id=6)

    pt28 = PostTag(post_id=13, tag_id=3)
    pt29 = PostTag(post_id=13, tag_id=6)

    pt30 = PostTag(post_id=14, tag_id=2)
    pt31 = PostTag(post_id=14, tag_id=3)
    pt32 = PostTag(post_id=14, tag_id=6)


    # Jake Jameson's posts
    pt33 = PostTag(post_id=15, tag_id=4)
    pt34 = PostTag(post_id=15, tag_id=5)

    pt35 = PostTag(post_id=16, tag_id=4)
    pt36 = PostTag(post_id=16, tag_id=5)

    pt37 = PostTag(post_id=17, tag_id=4)
    pt38 = PostTag(post_id=17, tag_id=5)


    db.session.add_all([pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10, pt11, pt12, pt13, pt14, pt15, pt16, pt17, pt18, pt19, pt20, pt21, pt22, pt23, pt24, pt25, pt26, pt27, pt28, pt29, pt30, pt31, pt32, pt33, pt34, pt35, pt36, pt37, pt38])
    db.session.commit()
