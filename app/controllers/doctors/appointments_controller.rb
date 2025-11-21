class Doctors::AppointmentsController < ApplicationController
  def index
    @appointments = Appointment.where(doctor: current_user)
  end

  def update
    @appointment = Appointment.find(params[:id])
    if @appointment.update(appointment_params)
      redirect_to doctors_appointments_path, notice: 'Appointment status updated.'
    else
      redirect_to doctors_appointments_path, alert: 'Failed to update appointment.'
    end
  end

  private

  def appointment_params
    params.require(:appointment).permit(:status, :note)
  end

  def current_user
    # Placeholder for authentication logic
    User.where(role: :doctor).first
  end
end
