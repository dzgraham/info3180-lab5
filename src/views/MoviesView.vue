<template>
  <div class="container mt-4">
    <h1 class="page-header mb-4">Movies</h1>
    
    <div v-if="movies.length === 0" class="alert alert-info">
      You haven't added any movies yet boss
    </div>
    
    <div class="movies-grid">
      <div v-for="movie in movies" :key="movie.id" class="movie-card">
        <div class="movie-poster">
          <img 
            :src="movie.poster" 
            :alt="movie.title"
            @error="handleImageError"
          />
        </div>
        <div class="movie-info">
          <h3 class="movie-title">{{ movie.title }}</h3>
          <p class="movie-description">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";

let movies = ref([]);

function handleImageError(event) {
  console.error("Image failed to load:", event.target.src);
  event.target.src = 'https://via.placeholder.com/120x160?text=No+Poster';
}

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

onMounted(() => {
  fetchMovies();
});
</script>

<style scoped>
.movies-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}

.movie-card {
  display: flex;
  border: 1px solid #ddd;
  height: 250px;
}

.movie-card:hover {
  background-color: #f9f9f9;
}

.movie-poster {
  width: 150px;
  background: #eee;
}

.movie-poster img {
  width: auto;
  height: 100%;
  object-fit: cover;
}

.movie-info {
  padding-left: 30px;
  overflow: hidden;
}

.movie-title {
  font-size: 22px;
  margin-bottom: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  overflow: hidden;
  text-overflow: ellipsis;
}

.movie-description {
  font-size: 18px;
  color: black;
  overflow: hidden;
}

@media (max-width: 600px) {
  .movies-grid {
    grid-template-columns: 1fr;
  }
}
</style>