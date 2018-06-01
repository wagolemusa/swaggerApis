from flask import Flask 
from flask_restplus import Api, Resource, fields

app  = Flask(__name__)
api  = Api(app)

a_languages = api.model('Language', {'language' : fields.String('The language')}) #, 'id' : fields.Integer('ID')

languages = []
python = {'language': 'Python', 'id' : 1}
languages.append(python)

@api.route('/language')
class Language(Resource):

    @api.marshal_with(a_languages, envelope='the_data')
    def get(self):
        return languages
    
    @api.expect(a_languages)
    def post(self):
        #languages.append(api.payload)
        new_language = api.payload
        new_language['id'] = len(languages) + 1
        languages.append(new_language)
        return {'result' :  'Language added'}, 201


if __name__ == '__main__':
    app.run(debug=True)