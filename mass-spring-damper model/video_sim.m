
clc
clear

%% system parames
dt = 1e-3; % simulation time step 
m1 = 70 * 1e-3; % finger mass
m2 = 34.05 * 1e-3; % key mass
% c0 = 10.5;
% c1 = 10.5;
% c2 = 10.5;
c0 = 0.5;
c1 = 0.5;
c2 = 0.3;
k2 =0.3012 * 1000; % key stiffness, N/m

%% UR5 Control params
depth = -20 * 1e-3; % m
% vel = 100 * 1e-3;   % m/s
acc = 1.0; %m/s^2
holdtime = 0;

% figure
pressure_list = [20,40,60,80];
pressure = 80;
% vel_list = [0.02,0.05,0.10];
vel_list = 0.10;
i = 1;

kf = 1.19*pressure+75.41;  
k1 = kf; % finger stiffness
k0 =kf; % finger stiffness 

for vel = vel_list
        
        %% Do simulation
    t_stop = 2*(-depth/vel+vel/(2*acc));
    disp(t_stop);
    res=sim('StateSpacev2','StartTime','0','StopTime',num2str(t_stop),'FixedStep',num2str(dt));
    
    time = res.tout;
    x0 = res.input.data;
    x1 = res.output.data(:,1);
    x2 = res.output.data(:,2);
    v0 = diff(x0)/dt;
    v1 = diff(x1)/dt;
    v2 = diff(x2)/dt;

                
    %     %% draw displacement of x0 x1 x2
    %     figure
    %     plot(time, x0,'y', 'linewidth',2)
    %     hold on
    %     plot(time, x1,'r', 'linewidth',2)
    %     hold on
    %     plot(time, x2,'b', 'linewidth',2)
    %     

    %     
    %     figure
    %     plot( v0,'y', 'linewidth',2)
    %     hold on
    %     plot( v1,'r', 'linewidth',2)
    %     hold on
    %     plot( v2,'b', 'linewidth',2)
        
%         fname = sprintf('model_output_p%dv%d.mat', pressure,vel);
%         save(fname,'time','x0','x1','x2','v0','v1','v2');
    end

save('videl_data.mat','time','x2');

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% %% draw FR response
% A = [0 1 0 0; 
%     -(k0+k1)/m1 -(c0+c1)/m1 k1/m1 c1/m1;
%     0 0 0 1; 
%     k1/m2 c1/m2 -1*(k1+k2)/m2 -1*(c1+c2)/m2];
% 
% B = [c0/m1;
%     k0/m1-(c0^2+c0*c1)/m1^2;
%     0;
%     c0*c1/(m1*m2)];
% 
% C = [1 0 0 0;
%     0 0 1 0];
% 
% D = [0;
%     0];
% 
% sys1 = ss(A,B,C,D);
% % sys1 = ss(A1,B1,C1,D1,'TimeUnit','seconds','InputUnit','seconds');
% omeg = logspace(-1,5); 
% sysg = frd(sys1,omeg); 
% bode(sysg,'r-');
