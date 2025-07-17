# 🧠 Project Workflow Overview

- **CV Component**: Deep learning model to detect and extract textual descriptions from medicine strips.
- **Adherence Agent**: Sends reminders via WhatsApp & Email, based on user prescription data.
- **Mobile Application**: Integrates both components with a user-friendly interface tailored for accessibility.

---

# 🗓️ Enhanced 4-Week Schedule

## 📅 Week 1: CV Model Training & Agent Improvements

### 🔍 CV Model
- [ ] Collect a high-quality dataset of medicine strips (real-world & synthetic)
- [ ] Preprocess data (resize, clean, augment, label using OCR/boxes)
- [ ] Train a baseline model (YOLOv8, EfficientDet, Detectron2, etc.)
- [ ] Evaluate model (mAP, precision/recall, error analysis)
- [ ] Fine-tune using hyperparameter tuning and transfer learning

### 🛎️ Adherence Agent
- [ ] Add retry mechanism for WhatsApp/Email failure
- [ ] Optimize Celery task frequency and query speed
- [ ] Explore cost-effective APIs or services (e.g., Mailgun, SMTP)
- [ ] Enable user-customized reminder frequency and message style

---

## 📅 Week 2: Backend Integration & Feature Enhancements

### 🔧 Backend Enhancements
- [ ] Add logging & monitoring (e.g., Prometheus/Grafana)
- [ ] Set up error tracking (e.g., Sentry)
- [ ] Implement role-based access control (RBAC)

### 🔐 Security & Accessibility
- [ ] Encrypt user emails, phone numbers, and sensitive data
- [ ] Enable API authentication (e.g., JWT)
- [ ] Add accessibility features (large fonts, voice alerts, one-tap interactions)

---

## 📅 Week 3: Mobile App Development

### 📱 App Frontend
- [ ] Choose stack (React Native or Flutter)
- [ ] Build pages:
  - [ ] User authentication
  - [ ] Prescription upload (camera integration)
  - [ ] Dashboard for reminders
  - [ ] Settings/Profile

### 🔗 Integration
- [ ] Connect app to Flask backend
- [ ] Display success/failure of reminders
- [ ] Send user-triggered test reminders

---

## 📅 Week 4: QA, Testing & Deployment

### 🧪 Testing
- [ ] Unit tests for all backend logic & CV model
- [ ] Integration tests (CV model with camera input)
- [ ] UI testing across Android & iOS devices

### 🚀 Deployment
- [ ] Containerize backend & Celery using Podman
- [ ] Setup CI/CD (GitHub Actions / Azure Pipelines)
- [ ] Internal testing & feedback collection
- [ ] Write complete setup & usage documentation

---

# ⚙️ Bonus: Parallelization Tips

- Let one teammate train the model while another improves backend features.
- Let frontend development start in parallel with backend integration.
