import axios from 'axios';

// Configurar Axios con la URL base
const api = axios.create({
    baseURL: 'http://localhost:8000/inmueble/crudPersona/',
    headers: {
        'Content-Type': 'application/json',
    }
});

// Funciones CRUD
export default {
    getAll() {
        return api.get('/');  // Obtener todos los registros
    },
    getById(id) {
        return api.get(`/${id}/`);  // Obtener un registro por ID
    },
    create(data) {
        return api.post('/', data);  // Crear un nuevo registro
    },
    update(id, data) {
        return api.put(`/${id}/`, data);  // Actualizar un registro
    },
    delete(id) {
        return api.delete(`/${id}/`);  // Eliminar un registro
    }
};
