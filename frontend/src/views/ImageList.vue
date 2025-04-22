<template>
  <div class="image-list">
    <div class="header">
      <h2>Image Gallery</h2>
      <router-link to="/upload" class="upload-btn">Upload New Image</router-link>
    </div>
    
    <div class="images-grid" v-if="images.length">
      <div v-for="image in images" :key="image.id" class="image-card">
        <img :src="'data:image/jpeg;base64,' + image.image_base64" :alt="image.description">
        <div class="image-info">
          <p>{{ image.description }}</p>
          <button @click="deleteImage(image.id)" class="delete-btn">Delete</button>
        </div>
      </div>
    </div>
    
    <div v-else class="no-images">
      <p>No images uploaded yet.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ImageList',
  data() {
    return {
      images: []
    }
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('/images/')
        this.images = response.data
      } catch (error) {
        console.error('Error fetching images:', error)
      }
    },
    async deleteImage(id) {
      if (confirm('Are you sure you want to delete this image?')) {
        try {
          await axios.delete(`/images/${id}/`)
          this.images = this.images.filter(image => image.id !== id)
        } catch (error) {
          console.error('Error deleting image:', error)
        }
      }
    }
  },
  mounted() {
    this.fetchImages()
  }
}
</script>

<style scoped>
.image-list {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.upload-btn {
  background-color: #42b983;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  text-decoration: none;
}

.images-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.image-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.image-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.image-info {
  padding: 1rem;
}

.delete-btn {
  background-color: #ff4444;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  cursor: pointer;
}

.delete-btn:hover {
  background-color: #cc0000;
}

.no-images {
  text-align: center;
  padding: 2rem;
  color: #666;
}
</style> 