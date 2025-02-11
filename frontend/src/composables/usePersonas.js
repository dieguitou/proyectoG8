import { ref, watch, onMounted } from 'vue';
import api from '@/services/api';

export function usePersonas() {
    const personas = ref([]);
    const todasLasPersonas = ref([]); // Para restaurar cuando el filtro esté vacío
    const nuevaPersona = ref({ nombrePersona: '', apellido: '', ci: '' });
    const personaEditando = ref(null);
    const filtroNombre = ref(''); // ✅ Estado para el filtro
    const cargando = ref(false);
    const error = ref(null);
    const mensaje = ref(null);

    // Cargar todas las personas
    const cargarPersonas = async () => {
        cargando.value = true;
        error.value = null;
        try {
            const response = await api.getAll();
            personas.value = response.data;
            todasLasPersonas.value = response.data; // Guardar copia de datos completos
        } catch (err) {
            error.value = 'Error al obtener la lista de personas.';
            console.error('Error al obtener personas:', err);
        } finally {
            cargando.value = false;
        }
    };

    // Filtrar personas mientras se escribe
    watch(filtroNombre, async (nuevoValor) => {
        if (!nuevoValor.trim()) {
            personas.value = todasLasPersonas.value; // Restaurar lista completa si el filtro está vacío
            return;
        }

        try {
            const response = await api.filterByName(nuevoValor);
            personas.value = response.data;
        } catch (err) {
            console.error('Error al filtrar personas:', err);
        }
    });

    // Seleccionar persona para edición
    const seleccionarPersona = (persona) => {
        personaEditando.value = { ...persona }; // Clonar para evitar mutaciones directas
    };

    // Guardar cambios de la persona editada
    const editarPersona = async () => {
        if (!personaEditando.value) return;

        try {
            await api.update(personaEditando.value.id, personaEditando.value);
            mensaje.value = "Persona editada exitosamente.";
            personaEditando.value = null; // Cerrar modal
            cargarPersonas(); // Recargar la lista con los cambios
        } catch (err) {
            error.value = "Error al editar persona.";
            console.error('Error al editar persona:', err);
        }
    };

    onMounted(cargarPersonas);

    return {
        personas,
        nuevaPersona,
        personaEditando,
        filtroNombre,
        cargando,
        error,
        mensaje,
        cargarPersonas,
        seleccionarPersona,
        editarPersona
    };
}
