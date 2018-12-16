from flask import Blueprint,render_template, current_app, request,redirect, url_for, flash
from website.decorators import admin_required
from website.models import DoubanMovie, db
from website.forms import MovieForm

admin=Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/movies')
@admin_required
def movies():
    page = request.args.get('page', default=1, type=int)
    pagination = DoubanMovie.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('admin/movies.html', pagination=pagination)

@admin.route('/movies/create', methods=['GET', 'POST'])
@admin_required
def create_movies():
    form=MovieForm()
    if form.validate_on_submit():
        form.create_movie()
        flash('创建成功', 'success')
        return redirect(url_for('admin.movies'))
    return render_template('admin/create_movie.html', form=form)

@admin.route('/movies/<int:movie_id>/edit', methods=['GET', 'POST'])
@admin_required
def edit_movies(movie_id):
    movie=DoubanMovie.query.get_or_404(movie_id)
    form=MovieForm(obj=movie)
    if form.validate_on_submit():
        form.update_movie(movie)
        flash('更新成功', 'success')
        return redirect(url_for('admin.movies'))
    return render_template('admin/edit_movie.html', form=form, movie=movie)

@admin.route('/movies/<int:movie_id>/delete')
@admin_required
def delete_movies(movie_id):
    movie=DoubanMovie.query.get_or_404(movie_id)
    db.session.delete(movie)
    db.session.commit()
    flash('电影“{}”删除成功'.format(movie.name), 'success')
    return redirect(url_for('admin.movies'))
