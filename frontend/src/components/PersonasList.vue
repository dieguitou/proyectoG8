<script setup>
import { usePersonas } from '@/composables/usePersonas';

const { personas, eliminarPersona } = usePersonas();
</script>

<template>
    <ul class="divide-y divide-gray-300">
        <li v-for="persona in personas" :key="persona.id"
            class="flex justify-between items-center p-4 bg-gray-100 rounded-lg shadow-md mb-4">
            <div>
                <p class="text-lg font-semibold text-gray-800">{{ persona.nombre }} ({{ persona.edad }} años)</p>
                <p class="text-gray-600">{{ persona.email }}</p>
            </div>
            <button @click="eliminarPersona(persona.id)"
                class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300">
                Eliminar
            </button>
        </li>
    </ul>
</template>

