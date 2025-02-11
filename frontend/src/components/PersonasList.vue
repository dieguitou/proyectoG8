<script setup>
import { ref } from 'vue';
import { usePersonas } from '@/composables/usePersonas';

const { personas, eliminarPersona, seleccionarPersona, personaEditando, editarPersona, filtroNombre } = usePersonas();
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
    <div>
        <!-- Mensaje de error si algo sale mal -->
        <p v-if="error" class="text-red-600 text-center mb-4">{{ error }}</p>

        <!-- Barra de búsqueda (filtro en tiempo real) -->
        <div class="mb-4 flex gap-2">
            <input v-model="filtroNombre" placeholder="Buscar por nombre..."
                class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none" />
        </div>

        <ul class="divide-y divide-gray-300">
            <li v-for="persona in personas" :key="persona.id"
                class="flex justify-between items-center p-4 bg-gray-100 rounded-lg shadow-md mb-4">
                <div>
                    <p class="text-lg font-semibold text-gray-800">
                        {{ persona.nombrePersona }} {{ persona.apellido }}
                    </p>
                    <p class="text-gray-600">CI: {{ persona.ci }}</p>
                </div>
                <div class="flex gap-2">
                    <button @click="seleccionarPersona(persona)"
                        class="bg-yellow-500 text-white px-4 py-2 rounded-lg hover:bg-yellow-600 transition duration-300">
                        Editar
                    </button>
                    <button @click="handleEliminar(persona.id)"
                        class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition duration-300">
                        Eliminar
                    </button>
                </div>
            </li>
        </ul>

        <!-- Modal de edición -->
        <div v-if="personaEditando" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
            <div class="bg-white p-6 rounded-lg shadow-lg w-96">
                <h2 class="text-2xl font-bold mb-4 text-gray-800">Editar Persona</h2>
                <input v-model="personaEditando.nombrePersona" placeholder="Nombre"
                    class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none mb-2" />
                <input v-model="personaEditando.apellido" placeholder="Apellido"
                    class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none mb-2" />
                <input v-model="personaEditando.ci" placeholder="CI" type="number"
                    class="w-full border rounded-lg p-3 text-gray-700 focus:ring-2 focus:ring-blue-500 outline-none mb-2" />

                <div class="flex justify-between mt-4">
                    <button @click="editarPersona"
                        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition duration-300">
                        Guardar Cambios
                    </button>
                    <button @click="personaEditando = null"
                        class="bg-gray-400 text-white px-4 py-2 rounded-lg hover:bg-gray-500 transition duration-300">
                        Cancelar
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>
