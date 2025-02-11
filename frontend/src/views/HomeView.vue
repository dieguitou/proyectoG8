<script setup>
import { ref } from 'vue';
import { usePersonas } from '@/composables/usePersonas';
import PersonasList from '@/components/PersonasList.vue';

const { nuevaPersona, agregarPersona, cargarPersonas } = usePersonas();
const mensaje = ref(null);
const error = ref(null);

// Función para manejar la creación de una persona
const handleAgregarPersona = async () => {
    mensaje.value = null;
    error.value = null;
    
    try {
        await agregarPersona();
        mensaje.value = "Persona agregada exitosamente.";
        cargarPersonas();  // Recargar la lista
    } catch (err) {
        error.value = "Error al agregar persona.";
        console.error("Error al agregar persona:", err);
    }
};
</script>

<template>
    <div class="max-w-3xl mx-auto p-6 bg-white shadow-lg rounded-lg mt-10">
        <h1 class="text-3xl font-bold text-center text-gray-800 mb-6">Gestión de Personas</h1>

        <!-- Mensajes de estado -->
        <p v-if="mensaje" class="text-green-600 text-center">{{ mensaje }}</p>
        <p v-if="error" class="text-red-600 text-center">{{ error }}</p>

        <!-- Formulario para agregar persona -->
        <div class="flex flex-col gap-4 mb-6">
            <input v-model="nuevaPersona.nombrePersona" placeholder="Nombre"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <input v-model="nuevaPersona.apellido" placeholder="Apellido"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <input v-model="nuevaPersona.ci" placeholder="CI" type="number"
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
            <button @click="handleAgregarPersona"
                class="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition duration-300">
                Agregar Persona
            </button>
        </div>

        
    </div>
</template>
