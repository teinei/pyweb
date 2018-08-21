
@app.route('/class/<int:class_id>/edit/', methods=['GET', 'POST'])
def editClass(class_id):
    editedClass = session.query(
        RiseClass).filter_by(id=class_id).one()
    if request.method == 'POST':
        if request.form['class_stage']:
            editedClass.class_stage = request.form['class_stage']
        #
        if request.form['class_name']:
            editedClass.class_name = request.form['class_name']
    
    session.add(editedClass)
    session.commit()