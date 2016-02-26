from flask import render_template, redirect, flash, url_for, Blueprint, session, request
from flask_login import login_user, current_user, login_required, logout_user
from flask_wtf import Form
from wtforms import PasswordField, SubmitField, StringField, BooleanField


class LoginForm(Form):
    username = StringField('username')
    password = PasswordField('password')
    submit = SubmitField('Login')
    remember = BooleanField('remember')
    is_loggedin = False


view = Blueprint('login', __name__)


@view.route('/login', methods=['GET', 'POST'])
def show():
    from monkey import UserModel
    form = LoginForm()
    form.is_loggedin = current_user is not None and not current_user.is_anonymous

    if form.validate_on_submit():
        #
        # ???
        #

        username, password = form.username.data, form.password.data
        print __name__ + ', uname: {0}, pwd: {1}'.format(username, password)
        user = UserModel.query.filter_by(
            username=username,
            password=password) \
            .first()

        if user is not None:
            session['remember'] = form.remember.data
            login_user(user, remember=form.remember.data)
            return redirect('/')

        form.username.errors.append('username or password not found')

    form.remember.data = session.get('remember', False)
    return render_template(
        'login.html', form=form
    )


@view.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    if request.method == 'POST':
        logout_user()
        return redirect(url_for('login.show'))
    return render_template('logout.html')
