<script setup>
import Navbar from '@/components/Navbar.vue';
import { RouterView } from 'vue-router';
</script>

<template>
    <Navbar />
    <div class="p-6">
        <RouterView />
    </div>
</template>
