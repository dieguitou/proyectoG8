import axios from 'axios';

// Configurar Axios con la URL base del backend
const api = axios.create({
    baseURL: 'http://localhost:8000/inmueble/',
    headers: {
        'Content-Type': 'application/json',
    }
});

// Funciones CRUD para personas
export default {
    // Listar todas las personas
    getAll() {
        return api.get('listPersona/');
    },

    // Crear una nueva persona
    create(data) {
        return api.post('listPersona/', data);
    },

    // Obtener detalles de una persona por ID
    getById(id) {
        return api.get(`crudPesonas/${id}/`);
    },

    // Editar una persona por ID
    update(id, data) {
        return api.put(`crudPesonas/${id}/`, data);
    },

    // Eliminar una persona por ID
    delete(id) {
        return api.delete(`crudPesonas/${id}/`);
    },

    // Filtrar personas por nombre
    filterByName(nombre) {
        return api.get(`/personas/filtradas/`, { params: { nombre } });
    }
};
