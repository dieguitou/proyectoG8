import { ref, onMounted } from 'vue';
import api from '@/services/api';

export function usePersonas() {
    const personas = ref([]);
    const nuevaPersona = ref({ nombre: '', edad: '', email: '' });

    // Cargar datos al montar el componente
    const cargarPersonas = async () => {
        try {
            const response = await api.getAll();
            personas.value = response.data;
        } catch (error) {
            console.error('Error al obtener personas:', error);
        }
    };

    // Crear una nueva persona
    const agregarPersona = async () => {
        try {
            await api.create(nuevaPersona.value);
            nuevaPersona.value = { nombre: '', edad: '', email: '' };
            cargarPersonas();
        } catch (error) {
            console.error('Error al agregar persona:', error);
        }
    };

    // Eliminar una persona
    const eliminarPersona = async (id) => {
        try {
            await api.delete(id);
            cargarPersonas();
        } catch (error) {
            console.error('Error al eliminar persona:', error);
        }
    };

    onMounted(cargarPersonas);

    return {
        personas,
        nuevaPersona,
        cargarPersonas,
        agregarPersona,
        eliminarPersona
    };
}
