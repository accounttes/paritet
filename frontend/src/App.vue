<template>
  <div id="app">
    <nav class="navbar">
      <h1>Image Management System</h1>
    </nav>
    <div class="container">
      <router-view></router-view>
    </div>
  </div>
</template>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

.navbar {
  background-color: #42b983;
  color: white;
  padding: 1rem;
  text-align: center;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}
</style> 