clc
clear 
load("forward_ctrl_data_v2.mat");
load("forward_ctrl_data_v3.mat")
colormap("parula")
%  patch(data(:,1),data(:,2),data(:,3),c,'FaceColor','none','EdgeColor','interp')
 scatter3(data(:,1),data(:,2),data(:,4),[],data(:,4),'.')
%  hold on
%  scatter3(data_small_vel(:,1),data_small_vel(:,2),data_small_vel(:,4),[],data_small_vel(:,4),'.')
 xlabel("Vacuum pressure (kPa)")
ylabel("UR5 velocity (m/s)")
zlabel("Hold time (s)")
 colorbar
 view(3)