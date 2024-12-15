

# TODO: Implement logic to fetch advertisements from the database
# For now, let's return fake database


from flask import Blueprint, request, url_for, jsonify

index_bp = Blueprint('index_api', __name__)

@index_bp.route('/get_advertisement', methods=['POST'])
def get_advertisement():
    request_data = request.get_json()
    limit = request_data.get('limit', 2)
    


    fake_db_advertisement_1 = {
        'title': 'Maximum comfort high-quality and performance.',
        'image_url': url_for('static', filename='img/main-page/advertisement/advertisement_1.jpg')
    }

    fake_db_advertisement_2 = {
        'title': '"Every journey begins with a bag."',
        'image_url': url_for('static', filename='img/main-page/advertisement/advertisement_2.jpg')
    }

    return jsonify([fake_db_advertisement_1, fake_db_advertisement_2])

@index_bp.route('/get_highlights', methods=['POST'])
def get_highlights():
    request_data = request.get_json()
    limit = request_data.get('limit', 4)


    fake_db_highlight_1 = {
        'title': 'The best of the best',
        'image_url': url_for('static', filename='img/main-page/highlights/highlight_1.png')
    }
    fake_db_highlight_2 = {
        'title': 'The best of the best',
        'image_url': url_for('static', filename='img/main-page/highlights/highlight_2.png')
    }
    fake_db_highlight_3 = {
        'title': 'The best of the best',
        'image_url': url_for('static', filename='img/main-page/highlights/highlight_3.png')
    }
    fake_db_highlight_4 = {
        'title': 'The best of the best',
        'image_url': url_for('static', filename='img/main-page/highlights/highlight_4.png')
    }

    return jsonify([fake_db_highlight_1, fake_db_highlight_2, fake_db_highlight_3, fake_db_highlight_4])