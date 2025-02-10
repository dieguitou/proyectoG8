<script setup>
import { usePersonas } from '@/composables/usePersonas';
import PersonasList from '@/components/PersonasList.vue';

const { nuevaPersona, agregarPersona } = usePersonas();
</script>

<template>
    <div class="max-w-3xl mx-auto p-6 bg-white shadow-lg rounded-lg mt-10">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Gestión de Personas</h1>

        <!-- Formulario para agregar persona -->
        <div class="flex flex-col gap-4 mb-6">
            <input v-model="nuevaPersona.nombre" placeholder="Nombre"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <input v-model="nuevaPersona.edad" placeholder="Edad" type="number"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <input v-model="nuevaPersona.email" placeholder="Email"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <button @click="agregarPersona"
                class="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition duration-300">
                Agregar Persona
            </button>
        </div>

        <!-- Componente de Lista de Personas -->
        <PersonasList />
    </div>
</template>
