<template>
  <div class="image-list">
    <div class="header">
      <h2>Список изображений</h2>
      <router-link to="/upload" class="upload-link">
        <i class="fas fa-plus"></i> Загрузить новое изображение
      </router-link>
    </div>
    
    <div v-if="loading" class="loading">
      <i class="fas fa-spinner fa-spin"></i> Загрузка...
    </div>
    
    <div v-else-if="images.length === 0" class="empty-state">
      <i class="fas fa-images"></i>
      <p>Нет загруженных изображений</p>
    </div>
    
    <div v-else class="image-grid">
      <div v-for="image in images" :key="image.id" class="image-card">
        <div class="image-container">
          <img :src="image.url" :alt="image.description" class="image" />
          <div class="image-overlay">
            <button @click="deleteImage(image.id)" class="delete-btn">
              <i class="fas fa-trash"></i>
            </button>
          </div>
        </div>
        <div class="image-description">
          {{ image.description || 'Без описания' }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ImageList',
  data() {
    return {
      images: [],
      loading: true,
      error: null
    };
  },
  async created() {
    await this.fetchImages();
  },
  methods: {
    async fetchImages() {
      try {
        const response = await axios.get('/images/');
        this.images = response.data;
      } catch (error) {
        console.error('Error fetching images:', error);
        this.error = 'Ошибка при загрузке изображений';
      } finally {
        this.loading = false;
      }
    },
    async deleteImage(id) {
      if (!confirm('Вы уверены, что хотите удалить это изображение?')) {
        return;
      }
      
      try {
        await axios.delete(`/images/${id}/`);
        this.images = this.images.filter(img => img.id !== id);
      } catch (error) {
        console.error('Error deleting image:', error);
        alert('Ошибка при удалении изображения');
      }
    }
  }
};
</script>

<style scoped>
.image-list {
  padding: 20px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.upload-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.upload-link:hover {
  background-color: #45a049;
}

.loading {
  text-align: center;
  padding: 40px;
  color: #666;
}

.empty-state {
  text-align: center;
  padding: 40px;
  color: #666;
}

.empty-state i {
  font-size: 48px;
  margin-bottom: 16px;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
}

.image-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  transition: transform 0.3s;
}

.image-card:hover {
  transform: translateY(-5px);
}

.image-container {
  position: relative;
  padding-top: 75%; /* 4:3 Aspect Ratio */
}

.image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.image-overlay {
  position: absolute;
  top: 10px;
  right: 10px;
  opacity: 0;
  transition: opacity 0.3s;
}

.image-card:hover .image-overlay {
  opacity: 1;
}

.delete-btn {
  background: rgba(255, 255, 255, 0.8);
  border: none;
  border-radius: 50%;
  width: 30px;
  height: 30px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
}

.delete-btn:hover {
  background: rgba(255, 255, 255, 1);
}

.image-description {
  padding: 12px;
  background: white;
  border-top: 1px solid #ddd;
}
</style> 