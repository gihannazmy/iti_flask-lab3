from crypt import methods

from flask import request, render_template, redirect, url_for

from app.posts import post_blueprint
from app.models import Post, db


@post_blueprint.route('', endpoint='index')
def index():
    posts = Post.query.all()
    return render_template("posts/index.html", posts=posts)

@post_blueprint.route('/create', methods=["GET","POST"], endpoint="create")
def create():
    if request.method == "POST":
        post = Post(name=request.form["name"], image=request.form["image"], description=request.form["description"])
        db.session.add(post)
        db.session.commit()
        return redirect(post.show_url)
    return render_template("posts/create.html")

@post_blueprint.route('/<int:id>', endpoint='show')
def show(id):
    post = db.get_or_404(Post, id)
    return render_template("posts/show.html", post=post)

@post_blueprint.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    post = db.get_or_404(Post, id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('post_blueprint.index'))
