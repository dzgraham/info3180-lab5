<template>
  <div class="container mt-4">
    <h1 class="page-header mb-4">Movies</h1>
    
    <div v-if="movies.length === 0" class="alert alert-info">
      You haven't added any movies yet boss
    </div>
    
    <div class="movies-grid">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <div class="card h-100">
          <img 
            :src="movie.poster" 
            class="card-img-top" 
            :alt="movie.title"
            @error="handleImageError"
          />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function fetchMovies() {
  fetch('/api/v1/movies')
    .then(response => response.json())
    .then(data => {
      console.log("Movies received:", data);
      movies.value = data.movies || [];
    })
    .catch(error => {
      console.error("Error fetching movies:", error);
    });
}

function handleImageError(event) {
  event.target.src = 'https://via.placeholder.com/300x400?text=No+Poster';
}

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  padding: 20px 0;
}

.movie-card:hover {
  outline: 2px solid #ccc;
}

.card-img-top {
  width: 100%;
  height: 400px;
}

.card-title {
  font-size: 18px;
  font-weight: 700;
}

.card-text {
  font-size: 14px;
  color: gray;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>