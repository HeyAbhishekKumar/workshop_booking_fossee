# FOSSEE Workshop Booking Portal Modernization

A premium, high-fidelity modernization of the FOSSEE Workshop Booking system, featuring a cutting-edge "Aurora" glassmorphism design language.

## 🚀 Overview

The FOSSEE Workshop Booking Portal has been transformed from a legacy interface into a state-of-the-art web application. The design focuses on "Liquid Glass" aesthetics, vibrant gradients, and a mobile-first responsive architecture.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/531cbb3f-223c-4d19-8fc6-954673b350c6" />


---

## 👥 Role-Based Features

### 🛠️ Administrator (Superuser)
The Admin maintains the backbone of the system with full control over the workshop ecosystem.
- **Workshop Type Management**: Create, edit, and delete various workshop modules.
- **Content Control**: Manage attachments, schedules, and terms & conditions for each workshop type.
- **Global Oversight**: Access the comprehensive Django Administrative suit to manage users, groups, and permissions.
- **System Statistics**: Monitor high-level portal analytics across all states and departments.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fc8cbed6-0454-436b-b4f9-38c54f4828b4" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/2b381dbc-1985-4fd3-9748-84e250959be6" />


---

### 🎓 Coordinator
Coordinators are the primary organizers who bridge the gap between institutes and FOSSEE.
- **Propose Workshops**: Submit detailed proposals for new workshops including preferred dates and types.
- **Status Tracking**: Monitor the real-time approval status of proposed workshops (Accepted/Pending/Rejected).
- **Profile Management**: Maintain professional credentials and institute details through a grid-based profile editor.
- **Data Analytics**: View public statistics to identify active regions and popular workshop types.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b46fc4d8-1b27-4f0f-bcfa-6a7323193d71" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/b3f336a7-3642-4316-9f25-6f8658c3d32e" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/c25a7919-4a4f-472b-9349-e3c4622b57ed" />


---

### 👨‍🏫 Instructor
Instructors are the subject matter experts responsible for delivering the workshop content.
- **Assignment View**: View and track workshops assigned to them by the administration.
- **Workshop Details**: Access deep details for assigned workshops, including coordinator info and dates.
- **Self-Service Profile**: Rapidly update security settings and personal information.
- **Unified Analytics**: Participate in the system-wide visual analytics to track historical delivery.

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/02fcda45-44e1-4695-8de0-9bcbd918e99a" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/0b32f749-40fa-4d69-bd19-d2b47c1c95a6" />


---

## 🔐 Test Credentials

For development and evaluation purposes, use the following accounts to test role-specific functionalities:

| Role | Username | Password |
| :--- | :--- | :--- |
| **Administrator** | `admin` | `fossee123` |
| **Coordinator** | `coordinator` | `fossee123` |
| **Instructor** | `instructor` | `fossee123` |

> [!NOTE]
> All passwords are set to `fossee123` for consistency across test roles.

---

## 🎨 Design & Development Insights

### 1. What design principles guided your improvements?
The modernization was guided by the **"Aurora Glass"** principle. This involves:
- **Depth & Translucence**: Utilizing `backdrop-filter: blur()` to create layers of information that feel physical and premium.
- **Visual Hierarchy**: Using vibrant HSL gradients and **"Electric Blue"** accents to draw attention to primary actions (Pill-shaped buttons).
- **Consistency**: Implementing a centralized design system in `base.css` ensuring that a form on the Login page looks identical to a form on the Profile page.

### 2. How did you ensure responsiveness across devices?
Responsiveness was achieved through:
- **CSS Grid Layouts**: The `register-form-grid` utility automatically switches from a 2-column desktop view to a stacked 1-column mobile view.
- **Dynamic Glass Panels**: All containers use percentage-based widths with `max-width` constraints to ensure they feel "natural" on ultra-wide monitors and smartphones alike.
- **Responsive Charts**: Integrated Auto-scaling logic in Chart.js ensure analytics modals adapt to the screen size without losing data clarity.

### 3. What trade-offs did you make between design and performance?
While premium glass effects can be GPU-intensive, I made the following strategic trade-offs:
- **Balanced Blurring**: Limited the `blur` radius to **25px** for common panels to maintain 60fps scrolling on mobile devices, while reserving heavier **40px** blurs for static overlays like Modals.
- **CSS-First Animations**: Used hardware-accelerated CSS transforms for the moving "Aurora dots" background rather than JavaScript animations, significantly reducing CPU overhead.

### 4. What was the most challenging part of the task?
The most challenging part was **Legacy Form Refactoring**. The original portal used rigid Bootstrap row/column structures hardcoded into templates.
- **Approach**: I extracted the logical form rendering from the HTML and created an abstract design system in `base.css`. By standardizing the `.form-control` and `.form-group` classes globally, I was able to modernize dozens of different forms (Login, Register, Profile, Propose) while writing minimal new HTML for each.

---

## 🖼️ Visual Showcase

### Before vs After

#### Login Page
*(Insert Before Screenshot)* -> <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5c973729-6ee6-4abd-a093-c5d9f33e5b8b" />


#### Workshop Statistics
*(Insert Before Screenshot)* -> <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/d5c67d33-6d38-4eb1-ba6c-098f95e83d0d" />


#### Propose Workshop (Calendar & Choice Bar)
*(Insert Before Screenshot)* -> ![Uploading image.png…]()


---

## 🛠️ Technology Stack
- **Frontend**: HTML5, Vanilla CSS3 (Custom Glassmorphism System), JavaScript
- **Framework**: Django 3.0.7
- **Visualization**: Chart.js 2.9, Google GeoCharts
- **Visual Palette**: Inter Font Family, Google Material Icons, Aurora Color Tokens
