<script setup>
import { useRoute, useRouter } from 'vue-router';

const route = useRoute();
const router = useRouter();

const goTo = (path) => {
    if (route.path !== path) {
        router.push(path);
    }
};
</script>

<template>
    <nav class="bg-blue-600 text-white p-4 shadow-lg w-full">
        <div class="max-w-5xl mx-auto flex justify-between items-center">
            <h1 class="text-xl font-bold">Gestión de Personas</h1>
            <ul class="flex gap-4">
                <li>
                    <button @click="goTo('/')" 
                        :class="{ 'font-bold underline': route.path === '/' }"
                        class="hover:text-gray-300 transition">
                        Inicio
                    </button>
                </li>
                <li>
                    <button @click="goTo('/personas')" 
                        :class="{ 'font-bold underline': route.path === '/personas' }"
                        class="hover:text-gray-300 transition">
                        Personas
                    </button>
                </li>
                <li>
                    <button @click="goTo('/about')" 
                        :class="{ 'font-bold underline': route.path === '/about' }"
                        class="hover:text-gray-300 transition">
                        About
                    </button>
                </li>
            </ul>
        </div>
    </nav>
</template>

