# SnapClass – AI-Powered Smart Attendance System

SnapClass makes classroom attendance fast. A teacher uploads one or more classroom photos, the app detects every face, matches each one against enrolled students, and records who was present and who was absent. No roll call needed.

**Live Demo:** https://snapclasss-digital-attendance.streamlit.app/



## Features

### For students
- **FaceID registration and login:** capture a photo with the camera, and the app creates a face embedding and signs you in on your next visit.
- **Join a subject** with a subject code, or by scanning the QR code or link shared by the teacher (auto-enrollment).
- **Dashboard** with enrolled subjects and attendance stats (total classes and classes attended).
- Unenroll from a subject at any time.
- Optional **voice enrollment** for voice-based attendance.

### For teachers
- Register and log in with a username and password (passwords are hashed with bcrypt).
- **Create subjects** and share the subject code or QR code with students.
- **Take attendance from photos:** add multiple classroom photos, run face analysis, and review the result before saving.
- **Voice attendance:** record students saying "I am present" and match the voices.
- **Attendance records** grouped by class session, with the full list of present and absent students for each session and a subject filter.
- **Delete a subject**, which also removes its enrollments and attendance records.

---

## How it works

```
Classroom photo
      │
      ▼
Face detection (dlib HOG detector)
      │
      ▼
Face landmarks + 128-d face embedding (dlib / face_recognition_models)
      │
      ▼
Compare with every enrolled student's embedding (Euclidean distance)
      │
      ├── closest match within threshold  →  student marked Present
      └── no match within threshold       →  face counted as unrecognized
```

- Each student has a **128-dimensional face embedding** stored in the database.
- For every detected face, the app finds the **nearest enrolled embedding** and accepts it only if the distance is below a threshold. Faces of people who are not enrolled are rejected instead of being force-matched to someone.
- **Voice attendance** uses speaker embeddings from [Resemblyzer](https://github.com/resemble-ai/Resemblyzer).
- Timestamps are stored in **UTC** and shown in **IST** in the attendance records.

---

## Tech stack

| Area | Technology |
|---|---|
| Language | Python |
| Web app | Streamlit |
| Face recognition | dlib, face_recognition_models, NumPy, scikit-learn |
| Voice recognition | Resemblyzer |
| Database | Supabase (PostgreSQL) |
| QR codes | Segno |
| Authentication | bcrypt |
| Data handling | Pandas, Pillow |
| Deployment | Streamlit Community Cloud |


## Privacy

SnapClass stores face and voice **embeddings** (numeric vectors) rather than raw photos. Only enroll people who have agreed to it, and restrict access to your database.


## Author

**Sumitra Choudhary**
B.E. Computer Science, M.B.M. University, Jodhpur
GitHub: [@sumitra63050](https://github.com/sumitra63050)
