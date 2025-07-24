# Event Management System (EMS)

A full-stack Django-based web application for organizing, managing, and registering for events. This system allows administrators to create and manage events while users can register, view, and participate in them. Styled with Bootstrap for a modern UI and enhanced with JavaScript feedback toasts.

---

## 🔧 Features

### ✅ User Functionality
- Register/Login/Logout securely
- View list of upcoming events
- Register/Unregister for events
- View personal registered events

### ⚙️ Admin Functionality
- Admin-only event creation, editing, and deletion
- Dashboard to view participant lists
- Role-based access control for Create/Edit/Delete

### 💡 UI Enhancements
- Responsive Bootstrap design
- Font Awesome icons
- JavaScript toast notifications for user actions

---

## 🛠 Technologies Used

- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Backend**: Python, Django 4.2
- **Database**: SQLite (default Django DB)
- **Tools**: Django Admin, Django ORM, Bootstrap Toasts

---

## 📁 Project Structure

event_management_system/
├── events/
│   ├── templates/events/
│   │   ├── base.html
│   │   ├── event_list.html
│   │   ├── event_detail.html
│   │   ├── create_event.html
│   │   ├── my_events.html
│   │   └── registration templates
│   ├── static/events/
│   │   └── styles.css
│   ├── views.py
│   ├── urls.py
│   ├── models.py
├── core/
│   ├── urls.py
├── manage.py
└── README.md

# Future Enhancements
	•	QR code for event check-in
	•	Email/SMS reminders
	•	Payment integration
	•	Certificate generation for event completion
