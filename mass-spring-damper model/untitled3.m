
clc
clear

%% system parames
dt = 1e-3; % simulation time step 
m1 = 7 * 1e-3; % finger mass
m2 = 34.05 * 1e-3; % key mass
% m1 = 70 * 1e-2; % finger mass
% m2 = 34.05 * 1e-2; % key mass
% c0 = 10.5;
% c1 = 10.5;
% c2 = 10.5;
c = 0.5;
c0 = c;
c1 = c;
c2 = 0.3;
% adaptive forward control model


%% UR5 Control params
depth = -30 * 1e-3; % m
% depth = -7 * 1e-3; % m
% vel = 100 * 1e-3;   % m/s
% acc = 1; %m/s^2 
% holdtime = 0.5;
holdtime = 0.5;
kf = 1.19*pressure+75.41;  
k1 = kf; % finger stiffness
k0 =kf; % finger stiffness 

load("forward_ctrl_data_v2");

sample_data = data(1:10,:);

k2 =0.3012 * 1000; % key stiffness, N/m
dk = 0.01 * 1000;
error = 100;
threshold = 0.005;

error = 0;
error_abs = 0;
while error>threshold
    if error_abs>0
        k2 = k2+dk;
    elseif error_abs<0
        k2 = k2-dk;
    end
    error = 0;
    error_abs = 0;
    for i = 1:len(data)        
        %% Do simulation
        t_stop = 2*-depth/vel+holdtime;
        disp(t_stop);
        res=sim('StateSpacev2','StartTime','0','StopTime',num2str(t_stop),'FixedStep',num2str(dt));
        
        time = res.tout;
        x0 = res.input.data;
        x1 = res.output.data(:,1);
        x2 = res.output.data(:,2);
        v0 = diff(x0)/dt;
        v1 = diff(x1)/dt;
        v2 = diff(x2)/dt;

        [min_x2,index_mx2] = min(x2);
        thres = -0.005;
        x2_half =  x2(1:round((size(x2,1)/2)));
        [ d, midi_down_poz] = min( abs( x2_half- thres) );
        midi = -1*v2(midi_down_poz(1));
        ht = sum(x2(:)<thres)*dt;
        error = error + (midi-data())^2;
        error_abs = error_abs + midi-data();
    end 
end 

for pressure = pressure_list
    kf = 1.19*pressure+75.41;  
    k1 = kf; % finger stiffness
    k0 =kf; % finger stiffness 
%     k2 = k2*0.065;
    k2 = k2*0.20;
    for vel = vel_list
        
        %% Do simulation
        t_stop = 2*-depth/vel+holdtime;
        disp(t_stop);
        res=sim('StateSpacev2','StartTime','0','StopTime',num2str(t_stop),'FixedStep',num2str(dt));
        
        time = res.tout;
        x0 = res.input.data;
        x1 = res.output.data(:,1);
        x2 = res.output.data(:,2);
        v0 = diff(x0)/dt;
        v1 = diff(x1)/dt;
        v2 = diff(x2)/dt;

        [min_x2,index_mx2] = min(x2);
        thres = -0.005;
%         thres = min_x2/5;
%         thres = -0.001;
        x2_half =  x2(1:round((size(x2,1)/2)));
        [ d, midi_down_poz] = min( abs( x2_half- thres) );
        midi = -1*v2(midi_down_poz(1));
        ht = sum(x2(:)<thres)*dt;

        data(i,:) = [pressure,vel,midi,ht];
        i = i+1;
                
    end
end

