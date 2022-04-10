from flask import Flask, request
app = Flask(__name__)
@app.route('/rate_receipt', methods=['POST'])
def rate_receipt():
    if request.method == 'GET':
        body = '''
            <form id="rating" action="/rate_receipt" method="POST">
            <label for=note>What is your note for the receipt?</label><br>
            <select id="nore" name="note">
            <option value="5">It is great!</option>
            <option value="4">It is very good</option>
            <option value="3" selected>It is just good</option>
            <option value="2">It was poor</option>
            <option value="1">It was horrible!</option>
            </select><br>
            <label for=comment>Write down your comments:</label><br>
            <textarea id="comment" name="comment" rows="3" cols="50">
            </textarea><br>
            <label for="decision">Would you cook it for your family?</label><br>
            <input type="checkbox" id="decision" name="decision"><br>
            <input type="submit" value="Share my feedback">
            </form>
            '''
        return body
    else:
        note = 3
        if 'note' in request.form:
            note = request.form['note']
        comment=''
        if 'comment' in request.form:
            comment = request.form['comment']
        decision = False
        if 'decision' in request.form:
            decision = True
        message = f'''Your rating was: {note}<br>
        Your comment was: {comment}<br>
        Your decision was {decision}
        '''
        return message