<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/">Graham</RouterLink>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <RouterLink 
                to="/" 
                class="nav-link"
                active-class="active"
                exact-active-class="active"
              >Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink 
                to="/about" 
                class="nav-link"
                active-class="active"
              >About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink 
                to="/movies" 
                class="nav-link"
                active-class="active"
              >Movies</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink 
                to="/movies/create" 
                class="nav-link"
                active-class="active"
              >Add Movie</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style>
.nav-link.active {
  font-weight: bold;
}
</style>