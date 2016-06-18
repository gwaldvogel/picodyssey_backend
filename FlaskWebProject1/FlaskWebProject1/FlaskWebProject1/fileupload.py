def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/uploadImage/<uuidPlace>', methods=['GET', 'POST'])
def upload_file(uuidPlace):
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			resizeImage(uuidPlace,str(app.config['UPLOAD_FOLDER'])+filename)
            return redirect(url_for('uploaded_file',
                                    filename=filename))