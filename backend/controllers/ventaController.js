import Venta from "../models/Venta.js"

const prueba = (req, res) => {

};
const createVentas = async (req, res) => {
    try {
        const venta = new Venta(req.body); const ventaGuardado = await venta.save(); res.json(ventaGuardado);
    } catch (error) {
        console.error(error.message);
    }

};
const getVenta = async (req, res) => {

};
const getVentas = async (req, res) => {

};
const updateVentas = async (req, res) => {
    try {
        const estadoVenta = await Venta.findById(req.params.id); if (estadoVenta.estado === "vigente") {
            estadoVenta.estado = "cancelada";
            await estadoVenta.save();
            res.json({
                msg: "Venta cancelada correctamente"
            });
        } else {
            res.json({
                msg: "La venta ya esta cancelada"
            });
        }
    } catch (error) {
        console.log(error.message);
    }
};


export {
    prueba,
    createVentas,
    getVenta,
    getVentas,
    updateVentas
    
};