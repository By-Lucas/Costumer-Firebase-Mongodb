// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
<script>
  <script src="https://www.gstatic.com/firebasejs/7.14.5/firebase-app.js"></script>
  <script src="https://www.gstatic.com/firebasejs/9.6.8/firebase-analytics.js"></script>
</script>
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyCw402ECAXr98Xfww1bGrPmB9bNEoll4-Q",
  authDomain: "login-8264d.firebaseapp.com",
  projectId: "login-8264d",
  storageBucket: "login-8264d.appspot.com",
  messagingSenderId: "411663390528",
  appId: "1:411663390528:web:2ffe7ff93dc250b668cca5",
  measurementId: "G-19562NHQRT"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);