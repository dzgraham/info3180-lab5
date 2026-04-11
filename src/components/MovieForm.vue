<template>
  <div class="movie-form-container">
    <!-- Success Message -->
    <div v-if="successMessage" class="alert alert-success alert-dismissible fade show" role="alert">
      {{ successMessage }}
      <button type="button" class="btn-close" @click="successMessage = ''"></button>
    </div>

    <!-- Error Messages -->
    <div v-if="errorMessages.length > 0" class="alert alert-danger alert-dismissible fade show" role="alert">
      <ul class="mb-0 mt-2">
        <li v-for="(error, index) in errorMessages" :key="index">
           {{ error }}
        </li>
      </ul>
      <button type="button" class="btn-close" @click="errorMessages = []"></button>
    </div>

    <form id="movieForm" @submit.prevent="saveMovie" enctype="multipart/form-data">
      <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input 
          type="text" 
          name="title" 
          id="title" 
          class="form-control"
          placeholder="Enter movie title"
        />
      </div>

      <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea 
          name="description" 
          id="description" 
          class="form-control" 
          rows="4"
          placeholder="Enter movie description"
        ></textarea>
      </div>

      <div class="form-group mb-4">
        <label for="poster" class="form-label">Photo Upload</label>
        <input 
          type="file" 
          name="poster" 
          id="poster" 
          class="form-control"
          accept=".jpg,.jpeg,.png,.gif"
        />
        <small class="text-muted">Allowed formats: JPG, JPEG, PNG, GIF</small>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let csrf_token = ref("");
let successMessage = ref("");
let errorMessages = ref([]);

function getCsrfToken() {
  fetch('/api/v1/csrf-token')
    .then(response => response.json())
    .then(data => {
      console.log("CSRF Token received:", data);
      csrf_token.value = data.csrf_token;
    })
    .catch(error => {
      console.error("Error fetching CSRF token:", error);
    });
}

function saveMovie() {
  let movieForm = document.getElementById('movieForm');
  let form_data = new FormData(movieForm);
  
  successMessage.value = "";
  errorMessages.value = [];
  
  fetch("/api/v1/movies", {
    method: 'POST',
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => response.json())
  .then(data => {
    console.log("Response:", data);
    if (data.errors) {
      errorMessages.value = data.errors;
    } else if (data.message) {
      successMessage.value = data.message;
      movieForm.reset();
    }
  })
  .catch(error => {
    console.error("Error:", error);
    errorMessages.value = [{ field: "general", message: "An error occurred. Please try again." }];
  });
}

onMounted(() => {
  getCsrfToken();
});
</script>

<style scoped>
.movie-form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
}
</style>