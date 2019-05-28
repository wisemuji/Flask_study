from werkzeug.datastructures import MultiDict

post = MultiDict()
post.add("foo", ["ham", "ham2"])
print(post)

post_copy = post.copy()
post_deepcopy = post.deepcopy()

post_copy["foo"].extend(["ham3"])
print(post)
post_deepcopy["foo"].extend(["ham4"])
print(post)