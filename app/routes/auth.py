from flask import Blueprint, render_template, url_for, request, redirect, flash, session

auth_bp = Blueprint('auth', __name__, template_folder='templates')

# Simulated user store
USER_CREDENTIALS = {
    'admin': '1234'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            session['user'] = username
            flash('Login successful.', 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash('Invalid username or password.', 'error')

    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")  # Not used in this basic version
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if username in USER_CREDENTIALS:
            error = "Username already exists."
            return render_template('register.html', error=error)

        if password != confirm_password:
            error = "Passwords do not match."
            return render_template('register.html', error=error)

        USER_CREDENTIALS[username] = password
        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')
