<script setup>
import { ref } from 'vue';
import { usePersonas } from '@/composables/usePersonas';
import PersonasList from '@/components/PersonasList.vue';

const { personas, eliminarPersona, filtroNombre, filtrarPersonas } = usePersonas();
const error = ref(null);

// Función para eliminar una persona con confirmación
const handleEliminar = async (id) => {
    if (!confirm("¿Estás seguro de que deseas eliminar a esta persona?")) return;

    try {
        await eliminarPersona(id);
    } catch (err) {
        error.value = "Error al eliminar la persona.";
        console.error("Error al eliminar:", err);
    }
};
</script>

<template>
    <!-- Componente de Lista de Personas -->
    <PersonasList />
</template>
