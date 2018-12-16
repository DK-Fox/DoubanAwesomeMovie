from flask import Blueprint,render_template, request, current_app
from website.models import DoubanMovie

movie=Blueprint('movie',__name__,url_prefix='/movie')

@movie.route('/')
def index():
    page=request.args.get('page', default=1, type=int)
    pagination=DoubanMovie.query.paginate(
        page=page,
        per_page=current_app.config['INDEX_PER_PAGE'],
        error_out=False
    )
    return render_template('movies_index.html',pagination=pagination)

@movie.route('/<int:id>')
def page_movies(id):
    movie=DoubanMovie.query.get_or_404(id)
    return render_template('movie.html',movie=movie)
