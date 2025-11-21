class Appointment < ApplicationRecord
  belongs_to :patient, class_name: 'User'
  belongs_to :doctor, class_name: 'User'
  enum :status, { pending: 0, confirmed: 1, cancelled: 2, completed: 3 }

  validate :doctor_not_double_booked

  private

  def doctor_not_double_booked
    return unless doctor_id && scheduled_at

    if Appointment.where(doctor_id: doctor_id, scheduled_at: scheduled_at).where.not(id: id).exists?
      errors.add(:scheduled_at, "is already booked for this doctor")
    end
  end
end
