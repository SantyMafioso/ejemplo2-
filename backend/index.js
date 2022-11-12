// https://expressjs.com/es/
import express from "express";
import dotenv from 'dotenv';
import cors from 'cors';
import fileupload from 'express-fileupload';

import conectarDB from './config/db.js';
import usuarioRoutes from './routes/UsuarioRoutes.js';
import productoRoutes from './routes/ProductoRoutes.js';
import ventaRoutes from './routes/VentaRoutes.js';

const PORT = process.env.PORT || 4000;
dotenv.config();
// Se le agrega toda la funcionalidad del servidor de express
const app = express();
app.use(express.json());

app.use(fileupload({
    useTempFiles: true,
    tempFileDir: './files'
}));
conectarDB();
// middlewares
// Se utiliza para realizar la comunicacion entre el servidor del frontend y el backend

const dominiosPermitidos = [process.env.FRONTEND_URL];
const corsOptions = {
    origin: function (origin, callback) {
        if (dominiosPermitidos.indexOf(origin) !== -1) {
            //El origen del Request esta permitido
            callback(null, true);
        } else {
            callback(new Error('No permitido por CORS'));
        }
    }
};
app.use(cors(corsOptions));

//GESTION DE USUARIOS//
app.use('/api/usuarios', usuarioRoutes);
//GESTION DE PRODUCTOS//
app.use('/api/productos', productoRoutes);
//GESTION DE VENTAS//
app.use('/api/ventas', ventaRoutes);
app.listen(PORT, () => {
    console.log(`Servidor funcionando en el puerto ${PORT} `);
});