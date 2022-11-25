import vtk
import numpy as np
from vtk.util import numpy_support

for i in range (0, 18):
    data = np.load('J:/Program/CT_VSGAN/gen_volume/221125_3_log_loss_vol_G_reg_L1_33_epoch_210/epoch_200_fake_V_' + str(i).zfill(2) + '.npy')

    data = data[:, :, :]
    # data = data / 255.
    imdata = vtk.vtkImageData()

    depthArray = numpy_support.numpy_to_vtk(data.ravel(order='F'), deep=True, array_type=vtk.VTK_FLOAT)

    imdata.SetDimensions([128, 128, 128])
    # fill the vtk image data object
    imdata.SetSpacing([1, 1, 1])
    imdata.SetOrigin([0, 0, 0])
    imdata.GetPointData().SetScalars(depthArray)

    writer = vtk.vtkMetaImageWriter()
    writer.SetFileName('J:/Program/CT_VSGAN/gen_volume/221125_3_log_loss_vol_G_reg_L1_33_epoch_210/epoch_200_fake_V_' + str(i).zfill(2) + '.mha')
    writer.SetInputData(imdata)
    writer.Write()