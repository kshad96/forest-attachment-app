from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)
stations = [
    { "name": "Esageri", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Maji Mazuri", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Narasha", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Chemususu", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Sabatia", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Kabarnet", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Kiptuget", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Tenges", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Koibatek", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Chemorgok", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Ol Arabel", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Chepalungu", "conservancy": "Mau", "county": "Bomet", "capacity": 3, "applicants": [] },
    { "name": "Itare", "conservancy": "Mau", "county": "Bomet", "capacity": 3, "applicants": [] },
    { "name": "Mara Mara", "conservancy": "Mau", "county": "Bomet", "capacity": 3, "applicants": [] },
    { "name": "Nyangores", "conservancy": "Mau", "county": "Bomet", "capacity": 3, "applicants": [] },
    { "name": "Kaberua", "conservancy": "Western", "county": "Bungoma", "capacity": 3, "applicants": [] },
    { "name": "Kaboywa", "conservancy": "Western", "county": "Bungoma", "capacity": 3, "applicants": [] },
    { "name": "Cheptongei", "conservancy": "North Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Kaptagat", "conservancy": "North Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Sabor", "conservancy": "N. Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Elgeyo", "conservancy": "North Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Penon", "conservancy": "North Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Kessup", "conservancy": "North Rift", "county": "Elgeiyo Marakwet", "capacity": 3, "applicants": [] },
    { "name": "Irangi", "conservancy": "Eastern", "county": "Embu", "capacity": 3, "applicants": [] },
    { "name": "Njukiini East", "conservancy": "Eastern", "county": "Embu", "capacity": 3, "applicants": [] },
    { "name": "Ngong Hills", "conservancy": "Nairobi", "county": "Kajiado", "capacity": 3, "applicants": [] },
    { "name": "Loitoktok", "conservancy": "Nairobi", "county": "Kajiado", "capacity": 3, "applicants": [] },
    { "name": "Kakamega", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Nzoia", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Lugari", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Turbo", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Malava", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Kericho", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Kerisoi", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Londiani", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Makutano", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Malagat", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Masaita", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Sorget", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Tendeno", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Kamae", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Kereita", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Kieni", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Kinale", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Muguga", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Ragia", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Thogoto", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Uplands", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Njukii-ni West", "conservancy": "Central", "county": "Kirinyaga", "capacity": 3, "applicants": [] },
    { "name": "Castle", "conservancy": "Central", "county": "Kirinyaga", "capacity": 3, "applicants": [] },
    { "name": "Kangaita", "conservancy": "Central", "county": "Kirinyaga", "capacity": 3, "applicants": [] },
    { "name": "Kathandeini", "conservancy": "Central", "county": "Kirinyaga", "capacity": 3, "applicants": [] },
    { "name": "Lariak", "conservancy": "Central", "county": "Laikipia", "capacity": 3, "applicants": [] },
    { "name": "NMarmanet", "conservancy": "Central", "county": "Laikipia", "capacity": 3, "applicants": [] },
    { "name": "Rumuruti", "conservancy": "Central", "county": "Laikipia", "capacity": 3, "applicants": [] },
    { "name": "Shamanek", "conservancy": "Central", "county": "Laikipia", "capacity": 3, "applicants": [] },
    { "name": "Iveti", "conservancy": "Eastern", "county": "Machakos", "capacity": 3, "applicants": [] },
    { "name": "Nthangu", "conservancy": "Eastern", "county": "Makueni", "capacity": 3, "applicants": [] },
    { "name": "Kilungu", "conservancy": "Eastern", "county": "Makueni", "capacity": 3, "applicants": [] },
    { "name": "Mbooni", "conservancy": "Eastern", "county": "Makueni", "capacity": 3, "applicants": [] },
    { "name": "Kibwezi", "conservancy": "Eastern", "county": "Makueni", "capacity": 3, "applicants": [] },
    { "name": "Mucheene", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Meru", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Nyambene", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Ontulili", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Lower Imenti", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Ruthumbi", "conservancy": "Eastern", "county": "Meru", "capacity": 3, "applicants": [] },
    { "name": "Gatare", "conservancy": "Central", "county": "Muranga", "capacity": 3, "applicants": [] },
    { "name": "Kimakia", "conservancy": "Central", "county": "Muranga", "capacity": 3, "applicants": [] },
    { "name": "Wanjerere", "conservancy": "Central", "county": "Muranga", "capacity": 3, "applicants": [] },
    { "name": "Karura", "conservancy": "Nairobi", "county": "Nairobi", "capacity": 3, "applicants": [] },
    { "name": "Ngong Road", "conservancy": "Nairobi", "county": "Nairobi", "capacity": 3, "applicants": [] },
    { "name": "Arboretum", "conservancy": "Nairobi", "county": "Nairobi", "capacity": 3, "applicants": [] },
    { "name": "Bahati", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Baraget", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Dundori", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Logoman", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Menengai", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Molo", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Mariashoni", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Sururu", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Kiptunga", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Ndoinet", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Saino", "conservancy": "Mau", "county": "Nakuru", "capacity": 3, "applicants": [] },
    { "name": "Cerengoni", "conservancy": "North Rift", "county": "Nandi", "capacity": 3, "applicants": [] },
    { "name": "North Nandi", "conservancy": "North Rift", "county": "Nandi", "capacity": 3, "applicants": [] },
    { "name": "Tinderet", "conservancy": "North Rift", "county": "Nandi", "capacity": 3, "applicants": [] },
    { "name": "Kimondi", "conservancy": "North Rift", "county": "Nandi", "capacity": 3, "applicants": [] },
    { "name": "Kapchorua", "conservancy": "North Rift", "county": "Nandi", "capacity": 3, "applicants": [] },
    { "name": "Geta", "conservancy": "Central", "county": "Nyandarua", "capacity": 3, "applicants": [] },
    { "name": "N.Kinangop", "conservancy": "Central", "county": "Nyandarua", "capacity": 3, "applicants": [] },
    { "name": "Ndaragwa", "conservancy": "Central", "county": "Nyandarua", "capacity": 3, "applicants": [] },
    { "name": "Ol bollossat", "conservancy": "Central", "county": "Nyandarua", "capacity": 3, "applicants": [] },
    { "name": "S. Kinangop", "conservancy": "Central", "county": "Nyandarua", "capacity": 3, "applicants": [] },
    { "name": "Chehe", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Gathiuru", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Hombe", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Kabaru", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Kiandogoro", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Kabage", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Muringato", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Zaina", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Naro Moru", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Nanyuki F.S", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Ragati", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Chogoria", "conservancy": "Eastern", "county": "Tharaka Nithi", "capacity": 3, "applicants": [] },
    { "name": "Chuka", "conservancy": "Eastern", "county": "Tharaka Nithi", "capacity": 3, "applicants": [] },
    { "name": "Kapenguria", "conservancy": "North Rift", "county": "West Pokot", "capacity": 3, "applicants": [] },
    { "name": "Kimothon", "conservancy": "North Rift", "county": "Trans nzoia", "capacity": 3, "applicants": [] },
    { "name": "Kiptogot", "conservancy": "North Rift", "county": "Trans Nzoia", "capacity": 3, "applicants": [] },
    { "name": "Kitale Township", "conservancy": "North Rift", "county": "Trans Nzoia", "capacity": 3, "applicants": [] },
    { "name": "Sosio", "conservancy": "North Rift", "county": "Trans Nzoia", "capacity": 3, "applicants": [] },
    { "name": "Saboti", "conservancy": "North Rift", "county": "Trans-Nzoia", "capacity": 3, "applicants": [] },
    { "name": "Suam", "conservancy": "North Rift", "county": "Trans-Nzoia", "capacity": 3, "applicants": [] },
    { "name": "Cengalo", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Kipkabus", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Lorenge", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Nabkoi", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Timboroa", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Kapsaret", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Kipkurere", "conservancy": "North Rift", "county": "Uasin Gishu", "capacity": 3, "applicants": [] },
    { "name": "Kibiri", "conservancy": "Western", "county": "Vihiga", "capacity": 3, "applicants": [] },
    { "name": "Wire", "conservancy": "Nyanza", "county": "Homa Bay", "capacity": 3, "applicants": [] },
    { "name": "Kodera", "conservancy": "Nyanza", "county": "Homa Bay", "capacity": 3, "applicants": [] },
    { "name": "Arabuko Sokoke", "conservancy": "Coast", "county": "Kilifi", "capacity": 3, "applicants": [] },
    { "name": "Kwale", "conservancy": "Coast", "county": "Kwale", "capacity": 3, "applicants": [] },
    { "name": "Buda", "conservancy": "Coast", "county": "Kwale", "capacity": 3, "applicants": [] },
    { "name": "Kefri Muguga", "conservancy": "Central", "county": "Kiambu", "capacity": 3, "applicants": [] },
    { "name": "Kefri Kakamega", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Kefri Turbo", "conservancy": "Western", "county": "Kakamega", "capacity": 3, "applicants": [] },
    { "name": "Kefri Maseno", "conservancy": "Nyanza", "county": "Kisumu", "capacity": 3, "applicants": [] },
    { "name": "Kefri Londiani", "conservancy": "Mau", "county": "Kericho", "capacity": 3, "applicants": [] },
    { "name": "Kefri Baringo", "conservancy": "Mau", "county": "Baringo", "capacity": 3, "applicants": [] },
    { "name": "Kefri Nyeri", "conservancy": "Central", "county": "Nyeri", "capacity": 3, "applicants": [] },
    { "name": "Kefri Kitui", "conservancy": "Eastern", "county": "Kitui", "capacity": 3, "applicants": [] },
    { "name": "KEFRI Gede", "conservancy": "Coast", "county": "Kilifi", "capacity": 3, "applicants": [] },
    { "name": "Kefri Rumuruti Laikipia", "conservancy": "Laikipia", "county": "Laikipia", "capacity": 3, "applicants": [] },
    { "name": "Kefri Karura Nairobi", "conservancy": "Nairobi", "county": "Nairobi", "capacity": 3, "applicants": [] }
]
from flask import render_template

@app.route('/admin')
def admin_page():
    return render_template('admin.html')

#admin login can be modified here
@app.route('/admin-login', methods=['POST'])
def admin_login():
    data = request.json
    # Change these credentials for your own secure use!
    if data["username"] == "admin" and data["password"] == "admin123":
        # Set session, etc. If you want real auth, use Flask-Login or similar!
        return jsonify({"success": True})
    return jsonify({"success": False, "msg": "Invalid credentials."})

@app.route('/admin-dashboard')
def admin_dashboard():
    # In practice, check for session/cookie first
    return render_template('admin-dashboard.html')

@app.route('/applications', methods=['GET'])
def applications():
    result = []
    for st in stations:
        for applicant in st['applicants']:
            record = {
                "name": applicant.get('name', ''),
                "admissionNo": applicant.get('admissionNo', ''),
                "gender": applicant.get('gender', ''),
                "email": applicant.get('email', ''),
                "phone": applicant.get('phone', ''),
                "class": applicant.get('class', ''),
                "station": st.get('name', ''),
                "conservancy": st.get('conservancy', ''),
                "county": st.get('county', '')
            }
            result.append(record)
    return jsonify({"success": True, "applications": result})


@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/stations')
def get_stations():
    return jsonify(stations)




@app.route('/apply', methods=['POST'])
def apply():
    data = request.json
    admission_no = data['admissionNo'].strip().upper()
    # Check if applicant already exists in any station
    for st in stations:
        for applicant in st['applicants']:
            if applicant['admissionNo'].strip().upper() == admission_no:
                msg = (
                    f"You have already applied for an attachment at {st['name']} Forest Station, "
                    f"{st['conservancy']} Conservancy, {st['county']} County."
                )
                return jsonify({"success": False, "msg": msg}), 400

    idx = int(data['stationIdx'])
    gender = data['gender']
    station = stations[idx]
    
    locked_gender = station['applicants'][0]['gender'] if station['applicants'] else None
    if locked_gender and locked_gender != gender:
        return jsonify({"success": False, "msg": "Station gender locked."}), 400

    if len(station['applicants']) >= station['capacity']:
        return jsonify({"success": False, "msg": "Station full."}), 400

    # Add the new applicant
    station['applicants'].append({
        "name": data['name'],
        "admissionNo": data['admissionNo'],
        "gender": data['gender'],
        "email": data['email'],
        "phone": data['phone'],
        "class": data['class']
    })

    return jsonify({"success": True, "msg": "Application successful!", "stations": stations})

@app.route('/lookup', methods=['POST'])
def lookup():
    data = request.json
    admission_no = data.get('admissionNo')
    for st in stations:
        for applicant in st['applicants']:
            if applicant['admissionNo'] == admission_no:
                result = {
                    "name": applicant['name'],
                    "admissionNo": applicant['admissionNo'],
                    "gender": applicant['gender'],
                    "email": applicant['email'],
                    "phone": applicant['phone'],
                    "class": applicant['class'],
                    "station": st['name'],
                    "conservancy": st['conservancy'],
                    "county": st['county']
                }
                return jsonify({"success": True, "data": result})
    return jsonify({"success": False, "msg": "No application found for that admission number."}), 404


if __name__ == '__main__':
    app.run(debug=True)
