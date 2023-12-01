package pamiw.eepw.notesapp.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pamiw.eepw.notesapp.entities.Note;

@Repository
public interface NoteRepository extends JpaRepository<Note, Long> {

}
